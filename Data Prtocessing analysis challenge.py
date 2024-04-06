# task 1
# Perform sentiment analysis on a collection of travel blog entries stored in travel_blogs.txt. 
# Identify and count the occurrences of positive words (e.g., "amazing", "enjoy", "beautiful") and 
# negative words (e.g., "bad", "disappointing", "poor").

# def analyze_blog_sentiments(blog_file):
#     # Implement sentiment analysis logic on the blog file
# Expected Outcome:
# A summary report indicating the number of positive and negative words in the travel blogs, 
# demonstrating the ability to process text data and apply basic sentiment analysis.

def analyze_blog_sentiments(blog_file):
    
    pos_words = ["amazing", "breathtaking", "enjoyed", "wonderful", "relaxed", "stunning", "memorable", "mesmerizing", "excellent", "delicious", "enlightening", "fantastic", "unforgettable"]
    neg_words = ["disappointing", "overcrowed", "poor", "lackluster", "scarce"]

    
    pos_count = 0
    neg_count = 0

    # Open the blog file and read its contents
    with open(blog_file, 'r') as file:
        print("hi")
        
        for review in file:
            print(review)
            # print(wrd)
            for wrd in pos_words:
                if wrd in review.lower():
                    pos_count += 1

            for wrd in neg_words:
                if wrd in review.lower():
                    neg_count += 1
                    
    print("There was ", pos_count, " positive words and ", neg_count, " negative words")

blog_name = input("Please input a blog name: ")
analyze_blog_sentiments(blog_name)




# task 2
# Compile and analyze historical weather data from multiple files (weather_2020.txt, 
# weather_2021.txt, etc.). Each file contains daily temperature data. Calculate the 
# average temperature for each year and identify the year with the highest average.

# def compile_weather_data(file_list):
#     # Aggregate temperature data and calculate the yearly averages
    
# Expected Outcome:
# An aggregated view of average temperatures for each year and identification of 
# the year with the highest average temperature, showcasing data aggregation and analysis skills.

def compile_weather_data(file_list):
    
    sum = 0
    temp_list = []
    year = ""
    temperature = 0
    
    with open(file_list, 'r') as file:
        
        for line in file:
            year, temperature = line.strip().split(',')

            temperature = int(temperature[:-3])
            
            print(temperature)
            year = year[:4]
            sum += temperature
            
            temp_list.append(temperature)
            
    avg = sum/len(temp_list)
            
    print("The year ", year, "had a average temperature of ", avg, " and the max temp being ", max(temp_list) )
    

# file_list = input("Enter file name: ")
# compile_weather_data(file_list)