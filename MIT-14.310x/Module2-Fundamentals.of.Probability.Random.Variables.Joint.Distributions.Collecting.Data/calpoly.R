library(rvest)
CPadmission <- read_html("https://admissions.calpoly.edu/prospective/profile.html")
CPadmission %>%
  html_nodes("table") %>%
  .[[1]]%>%
  html_table()

admission_1<-html_table(CPadmission)

CPadmission %>%
  html_nodes("table") %>%
  .[[2]]%>%
  html_table()

admission_2<-html_table(CPadmission)