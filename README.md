# RTMS
Ristvedt Ticket Management System

## Install
* python 3.11!!!!
* https://visualstudio.microsoft.com/visual-cpp-build-tools/
* https://mariadb.com/downloads/connectors/
* pip install mysqlclient

# Ristvedt Ticket Management System (RTMS)

## Data
* User table
    * user id (primary unqiue)
    * user name
    * user level
* Ticket table
    * ticket number (primary unique)
    * ticket title
    * ticket description
    * ticket status
    * ticket priority
    * ticket precedence
    * ticket requester
    * ticket plant
    * ticket assigned to
    * ticket created date
    * ticket goal date
    * ticket completed date
    * ticket branch
* Task table
    * ticket number (foreign, primary, unique)
    * task number            (primary, unique)
    * task title
    * task description
    * task status
    * task precedence 
    * task plant
    * task assigned to
    * task created date
    * task goal date
    * task completed date
    * task branch
* Comment table
    * comment table
    * comment id
    * comment 
    
## Design Considerations
* LDAP authentication
* Web server and interface?
* Standalone executable?

