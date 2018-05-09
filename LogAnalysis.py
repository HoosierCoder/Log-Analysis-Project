#! /usr/bin/env python3

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


def getQueryResults(query):

    """
    getQueryResults() takes a query string as an
    arguemet, and executes the query via
    the psycopg2 library, then returns
    the results
    """
    db = psycopg2.connect("dbname=news")
    mycursor = db.cursor()
    mycursor.execute(query)
    results = mycursor.fetchall()
    db.close()
    return results

def printQueryResults(results, title):

    """
    printQueryResults() takes a query result and
    string value as arguemets, and prints out
    first the query results title, then
    the query results.
    """
    
    print('\n');
    print(title)
    for row in results:
        print("%s - %s views" % (row[0], row[1]))

def printErrorQueryResults(results, title):

    """
    printErrorQueryResults() takes a query result and
    string value as arguemets, and prints out
    first the query results title, then
    the query results.  Since the error results
    query needs to be formatted differenty
    than the other query results, the method
    was created to handle the differences.
    """
    print('\n');
    print(title)
    for row in results:
        print '\t' + '\t' + str(row[0]) + " - " \
        + str(Decimal(row[1]).quantize(Decimal('.01'), rounding=ROUND_UP)) \
        + "%"
        

articlesResults = getQueryResults(mostPopularArticlesQuery)
printQueryResults(articlesResults, "\tMost Popular Articles")

authorsResults = getQueryResults(mostPopularAuthorsQuery)
printQueryResults(authorsResults, "\tMost Popular Authors")

onePercentErrorDays = getQueryResults(onePercentErrorDaysQuery)
printErrorQueryResults(onePercentErrorDays, \
                       "\tDays With More Than One Percent Failed Hits")

