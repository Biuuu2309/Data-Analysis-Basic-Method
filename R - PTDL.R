install.packages("tidyverse")
library(tidyverse)
library(ggplot2)
library(dplyr)
library(lubridate)
install.packages("hrbrthemes")
library(hrbrthemes)
library(tidyr)
library(viridis)
install.packages("plotly")
library(plotly)
install.packages("gapminder")
library(gapminder)
install.packages("ggridges")
library(ggridges)
install.packages("GGally")
library(GGally)

#Scatter chart 
ggplot(data = Youtube, aes(x = likes, y = views)) +
  geom_point(color = "#FFA500", size = 1) +
  labs(title = "Scatter chart: Mối quan hệ giữa likes và views", x = "Likes", y = "Views") +
  theme_light()

#Barplot chart 
ggplot(data = Youtube, aes(x = publish_country, y = views)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Barplot chart: Lượt xem theo quốc gia xuất bản", x = "Publish country", y = "Views") +
  theme_minimal()

#Pie chart
Youtube_s1 <- Youtube %>%
  group_by(published_day_of_week) %>%
  summarize(total_views = sum(views)) %>%
  mutate(fraction = total_views / sum(total_views),
         percentage = round(fraction * 100, 1),
         ymax = cumsum(fraction),
         ymin = c(0, head(ymax, n = -1)),
         label_position = (ymax + ymin) / 2,
         label = paste0(percentage, "%"))

ggplot(data = Youtube_s1, aes(ymax = ymax, ymin = ymin, xmax = 4, xmin = 3, fill = published_day_of_week)) +
  geom_rect() +
  geom_text(aes(x = 3.5, y = label_position, label = label), size = 4, color = "white") +
  coord_polar(theta = "y") +
  theme_void() +
  theme(legend.position = "right") +
  labs(title = "Pie Chart: Views by Published Day of the Week",
       fill = "Day of the Week")

#Doughnut chart
Youtube_s2 <- Youtube %>%
  group_by(publish_country) %>%
  summarize(total_views = sum(views)) %>%
  mutate(fraction = total_views / sum(total_views),
         percentage = round(fraction * 100, 1),
         ymax = cumsum(fraction),
         ymin = c(0, head(ymax, n = -1)),
         label_position = (ymax + ymin) / 2,
         label = paste0(percentage, "%"))

ggplot(data = Youtube_s2, aes(ymax = ymax, ymin = ymin, xmax = 4, xmin = 3, fill = publish_country)) +
  geom_rect() +
  geom_text(aes(x = 3.5, y = label_position, label = label), size = 4, color = "white") +
  coord_polar(theta = "y") +
  theme_void() +
  xlim(c(2, 4)) +  
  theme(legend.position = "right") +
  labs(title = "Doughnut Chart: Views by Country",
       fill = "Country")

#Line chart
daily_views <- Youtube %>%
  group_by(time_frame) %>%
  summarise(views = mean(views, na.rm = TRUE))  

ggplot(daily_views, aes(x = time_frame, y = views)) +
  geom_line(group = 1, color = "blue") +  
  geom_point(color = "red", size = 2) +   
  labs(title = "Line chart: Views by Day of Week", 
       x = "Day of Week", 
       y = "Average Views") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
  
#Violin chart
ggplot(Youtube, aes(x = publish_country, y = category_id, fill = publish_country)) +
  geom_violin() +  
  labs(title = "Violin chart: Species videos each of country", 
       x = "Country", 
       y = "Category ID") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

#Density chart
ggplot(data=Youtube, aes(x=category_id, group=publish_country, fill=publish_country)) +
  geom_density(adjust=1.5, position="fill") +
  theme_ipsum() +
  labs(title = "Density chart: About species videos of country")
  theme_minimal() +

#Boxplot chart 
Youtube %>%
  mutate(publish_country = fct_reorder(publish_country, category_id, .fun = 'median')) %>%
  ggplot(aes(x = publish_country, y = category_id, fill = publish_country)) + 
  geom_boxplot() +
  labs(title = "Boxplot chart: About Category Id and Country sort by median",
    x = "Publish Country",
    y = "Category ID") +
  theme_minimal() +
  theme(legend.position = "none", axis.text.x = element_text(angle = 45, hjust = 1))

#Basic ridgeline plot
data <- Youtube %>%
  filter(!is.na(category_id))

ggplot(data, aes(x = category_id, y = published_day_of_week, fill = published_day_of_week)) +
  geom_density_ridges(scale = 1.5, rel_min_height = 0.01, alpha = 0.7) +
  scale_fill_brewer(palette = "Set3") +  # Sử dụng bảng màu
  labs(
    title = "Ridgeline Plot: Distribution of Views by Day of Week",
    x = "Views",
    y = "Published Day of Week"
  ) +
  theme_ridges() +
  theme(
    legend.position = "none",   
    axis.text.x = element_text(angle = 45, hjust = 1) 
  )

#Correlation
data <- Youtube %>%
  select(views, likes, dislikes, comment_count)  

ggpairs(
  data,
  lower = list(continuous = "smooth"), 
  diag = list(continuous = "barDiag"), 
  upper = list(continuous = "cor")    
) +
  labs(title = "Correlation Plot for Youtube Data") +
  theme_minimal()

#5 đồ thị dựa trên dữ liệu tổng hợp
#Stacked barplot
data <- Youtube %>%
  group_by(published_day_of_week, time_frame) %>%
  summarise(count = n(), .groups = "drop")  

ggplot(data, aes(x = published_day_of_week, y = count, fill = time_frame)) +
  geom_bar(stat = "identity", position = "stack") +
  scale_fill_viridis_d(name = "Time Frame") +  
  labs(
    title = "Stacked Barplot: Counts by Day of Week and Time Frame",
    x = "Day of Week",
    y = "Count"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "right"
  )

#Circular barplot
data <- Youtube %>%
  group_by(time_frame) %>%
  summarise(avg_views = mean(views, na.rm = TRUE), .groups = "drop")

data <- data %>%
  arrange(desc(avg_views)) %>%
  mutate(time_frame = factor(time_frame, levels = unique(time_frame)))

ggplot(data, aes(x = time_frame, y = avg_views, fill = time_frame)) +
  geom_bar(stat = "identity") +  
  coord_polar(theta = "x") +  
  scale_fill_viridis_d(name = "Time Frame") + 
  labs(
    title = "Circular Barplot: Average Views by Time Frame",
    x = "",
    y = "Average Views"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1),  
    legend.position = "none" 
  )

#Heatmap chart
data <- Youtube %>%
  group_by(time_frame, published_day_of_week) %>%
  summarise(total_views = sum(views, na.rm = TRUE), .groups = 'drop')

ggplot(data, aes(x = time_frame, y = published_day_of_week, fill = total_views)) +
  geom_tile(color = "white") +  
  scale_fill_gradient(low = "lightblue", high = "darkblue", name = "Total Views") +
  labs(
    title = "Heatmap: Total Views by Time Frame and Day of week ",
    x = "Time Frame",
    y = "Day Of Week"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1)
  )

#Area chart
data <- Youtube %>%
  group_by(time_frame) %>%
  summarise(avg_views = mean(views, na.rm = TRUE), .groups = "drop")

ggplot(data, aes(x = time_frame, y = avg_views, group = 1, fill = time_frame)) +
  geom_area(alpha = 0.6, color = "black", size = 0.5) +  
  scale_fill_brewer(palette = "Set3") + 
  labs(
    title = "Area Chart: Average Views by Time Frame",
    x = "Time Frame",
    y = "Average Views"
  ) +
  theme_minimal() +
  theme(
    axis.text.x = element_text(angle = 45, hjust = 1),
    legend.position = "none" 
  )

#Bubble chart
data <- Youtube %>%
  group_by(publish_country, time_frame) %>%
  summarise(views = sum(views), .groups = 'drop') %>%
  mutate(
    time_frame = factor(time_frame, levels = unique(time_frame)),  # Giữ thứ tự
    text = paste("Country: ", publish_country,
                 "\nTime Frame: ", time_frame,
                 "\nViews: ", views, sep = "")
  )

p <- ggplot(data, aes(x = time_frame, y = views, size = views, color = publish_country, text = text)) +
  geom_point(alpha = 0.7) +
  scale_size(range = c(2, 20), name = "Views") +
  scale_color_viridis(discrete = TRUE) +
  labs(
    title = "Bubble Chart: Views by Published Country and Time Frame",
    x = "Time Frame",
    y = "Views"
  ) +
  theme_minimal() +
  theme(
    legend.position = "right",
    axis.text.x = element_text(angle = 45, hjust = 1)
  )
pp <- ggplotly(p, tooltip = "text")
pp