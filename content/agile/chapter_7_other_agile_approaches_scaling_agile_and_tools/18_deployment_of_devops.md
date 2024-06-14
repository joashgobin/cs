# Deployment of DevOps
The common signs of distancing between Dev and Ops are:
- we do not discover bugs in software until well into the life cycle
- we are agile in development but not in release to production
- developers and/or testers cannot simulate production
- it is not possible to determine which problems arose in development, tests or already in production
- there is talk of "many human mistakes" during development and deployment
- dev considers their work to be done once deployed in preproduction
- every time a problem appears, we see "finger pointing"

## Some steps towards DevOps
- form work groups with people covering Dev+Ops+QA
- improve the agile environment
- analyze the development and release life cycle, gaps, metrics, etc.
- evaluate new technologies to automate deployments, tests, metric collection, etc.
- correctly select the first application or line of business to implement DevOps - the one with the most delays or problems
- get quick wins and give visibility to DevOps

## Some tips and good practices
- event management must share many events with development, not just with operations
- design the infrastructure to respond to functional requirements, not the other way around
- have pre-production environments
- the same team for development will do "level 2" for incidents
- Scrum or pair programming for development
- consider ITIL
- metrics:
    - number of releases per unit of time
    - escaped defects
    - operations backlog (releases pending to be carried out in production)
    - MTRS (also MTTR)
    - SLAs compliance
- "shifting left" - do normal work earlier in the work cycle
- continuous integration
- bidirectional information exchange between Operations and Development
