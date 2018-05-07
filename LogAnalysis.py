# "Log Analysis" for the Log Analysis Project for
# Udacity Full Stack Developer Nanodegree

import datetime
import psycopg2
from decimal import Decimal
from decimal import ROUND_UP

mostPopularArticlesQuery = """select articles.title, count(*) as num
            FROM log, articles
            WHERE log.status='200 OK'
            AND log.path LIKE '%' || articles.slug || '%'
            GROUP BY articles.title
            ORDER BY num desc
            LIMIT 3"""

mostPopularAuthorsQuery = """SELECT name, num FROM topauthors"""

onePercentErrorDaysQuery = """SELECT tdate, rate
                            FROM dayerrorpercents
                            WHERE rate > 1"""

def getMostPopularArticles():
    db = psycopg2.connect("dbname=news")
    mycursor = db.cursor()
    mycursor.execute(mostPopularArticlesQuery)
    results = mycursor.fetchall()
    db.close()
    return results

def getMostPopularAuthors():
    db = psycopg2.connect("dbname=news")
    mycursor = db.cursor()
    mycursor.execute(mostPopularAuthorsQuery)
    results = mycursor.fetchall()
    db.close()
    return results


def getOnePercentErrorDays():
    db = psycopg2.connect("dbname=news")
    mycursor = db.cursor()
    mycursor.execute(onePercentErrorDaysQuery)
    results = mycursor.fetchall()
    db.close()
    return results

def printQueryResults(results, title):
    print('\n');
    print(title)
    for row in results:
        print("%s - %s views" % (row[0], row[1]))

def printErrorQueryResults(results, title):
    print('\n');
    print(title)
    for row in results:
        print '\t' + '\t' + str(row[0]) + " - " + str(Decimal(row[1]).quantize(Decimal('.01'), rounding=ROUND_UP)) + "%"
        

articlesResults = getMostPopularArticles()
printQueryResults(articlesResults, "\tMost Popular Articles")

authorsResults = getMostPopularAuthors()
printQueryResults(authorsResults, "\tMost Popular Authors")

onePercentErrorDays = getOnePercentErrorDays()
printErrorQueryResults(onePercentErrorDays, "\tDays With More Than One Percent Failed Hits")
