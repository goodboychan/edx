library(rvest)
library(tidyr)
library(dplyr)

larecherche <- read_html("https://www.abebooks.com/servlet/SearchResults?pt=book&sortby=17&tn=a+la+recherche+du+temps+perdu&an=proust&cm_sp=pan-_-srp-_-ptbook")

price <- larecherche %>%
  html_nodes(".item-price .price") %>%
  html_text() %>%
  readr::parse_number()

title <- larecherche %>%
  html_nodes(".col-xs-8 a span") %>%
  html_text() %>%
  readr::parse_character()

combined <- data_frame(title, `data and time`=Sys.time(), price)