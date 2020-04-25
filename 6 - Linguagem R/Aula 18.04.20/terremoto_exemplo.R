## Aplicação Web!!!
# Dataset reference: https://www.kaggle.com/usgs/earthquake-database/data

### Limpando Plots, Console and Ambiente
rm(list = ls())
dev.off(dev.list()["RStudioGD"])
cat("\014")

#install.packages("shiny")
#install.packages("leaflet")
#install.packages("dplyr")

# Escolher diretório e pasta dos dados
setwd("database.csv")

#load libraries
library(shiny)
library(leaflet)
library(dplyr)
library(leaflet.extras)#import data
data <- read.csv("database.csv")

#categorize earthquake depth
data$depth_type <- ifelse(data$Depth <= 70, "shallow", ifelse(data$Depth <= 300 | data$Depth >70, "intermediate", ifelse(data$Depth > 300, "deep", "other")))

# UI and Server
ui <- fluidPage(
  mainPanel( 
    #this will create a space for us to display our map
    leafletOutput(outputId = "mymap"), #this allows me to put the checkmarks ontop of the map to allow people to view earthquake depth or overlay a heatmap
    absolutePanel(top = 100, left = 60, 
                  checkboxInput("markers", "Depth", FALSE),
                  checkboxInput("heat", "Heatmap", FALSE)
    )
  ))

server <- function(input, output, session) {
  
  #define the color pallate for the magnitidue of the earthquake
  pal <- colorNumeric(
    palette = c('gold', 'orange', 'dark orange', 'orange red', 'red', 'dark red'),
    domain = data$Magnitude)
  
  #define the color of for the depth of the earquakes
  pal2 <- colorFactor(
    palette = c('blue', 'yellow', 'red'),
    domain = data$depth_type
  )
  
  #create the map
  output$mymap <- renderLeaflet({
    leaflet(data) %>% 
      setView(lng = -99, lat = 45, zoom = 2)  %>% #setting the view over ~ center of North America
      addTiles() %>% 
      addCircles(data = data, lat = ~ Latitude, lng = ~ Longitude, weight = 1, radius = ~sqrt(Magnitude)*25000, popup = ~as.character(Magnitude), label = ~as.character(paste0("Magnitude: ", sep = " ", Magnitude)), color = ~pal(Magnitude), fillOpacity = 0.5)
  })
  
#next we use the observe function to make the checkboxes dynamic. 
#If you leave this part out you will see that the checkboxes, when clicked 
#on the first time, display our filters...But if you then uncheck them they stay on. 
#So we need to tell the server to update the map when the checkboxes are unchecked.

  observe({
    proxy <- leafletProxy("mymap", data = data)
    proxy %>% clearMarkers()
    if (input$markers) {
      proxy %>% addCircleMarkers(stroke = FALSE, color = ~pal2(depth_type), fillOpacity = 0.2,      label = ~as.character(paste0("Magnitude: ", sep = " ", Magnitude))) %>%
        addLegend("bottomright", pal = pal2, values = data$depth_type,
                  title = "Depth Type",
                  opacity = 1)}
    else {
      proxy %>% clearMarkers() %>% clearControls()
    }
  })
  
  observe({
    proxy <- leafletProxy("mymap", data = data)
    proxy %>% clearMarkers()
    if (input$heat) {
      proxy %>%  addHeatmap(lng=~Longitude, lat=~Latitude, intensity = ~Magnitude, blur =  10, max = 0.05, radius = 15) 
    }
    else{
      proxy %>% clearHeatmap()
    }
    
  })
  
}
  
shinyApp(ui, server)
