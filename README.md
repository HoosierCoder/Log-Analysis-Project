# Log-Analysis-Project
Read the news database and display information relating to views

*coding performed by Dennis A. Johns*

# Nanodegree
Udacity's Full Stack Developer

The log analysis project is first database project assigned for Udacity's Full Stack Web Devloper nanodegree!

# What is this project, anyhow?

The Full Stack Web Developer Log Analysis project to report data pertaining to the NEWS database.

# Requirements to run the program

Before the user can execute this program, there are a few things to be done first:
- Download the source files from this branch
- Install Python 3 on your local computer
- Install the Vagrant and VirtualBox tools
- Ensure the newsdata.sql file is loaded in the directory

# Views created

- topauthors
```
create view topauthors as
select authors.name, count(*) as num
            from articles, authors, log
            where authors.id = articles.author
            and log.path like '%' || articles.slug || '%'
	    and log.status like '%200%'
            group by authors.name
            order by num desc;
```           
- dayerrors
```
create view dayerrors as
SELECT cast(time as date) as tdate, count(*) as tally FROM log 
     WHERE status like '%404%' 
     GROUP BY tdate
     ORDER BY tally desc;
```
- daytotals
```
create view daytotals as
SELECT count(*) as tally, cast(time as date) as tdate FROM log GROUP BY tdate;
```
- dayerrorpercents
```
create view dayerrorpercents as
select daytotals.tdate, daytotals.tally as dailyhits, 
dayerrors.tally as dailyfails, 
(dayerrors.tally::double precision)*100/daytotals.tally::double precision as rate
from daytotals, dayerrors 
where daytotals.tdate=dayerrors.tdate
order by rate desc;
```
# Now that you have the requirements installed...

- Download the zip file containing the project files
- Unzip the project files to a directory of your choice
- navigate to this directory and type vagrant up
- From the same directory type vagrant ssh
- Run the program by typing Python LogAnalysis.py
