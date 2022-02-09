# Option 2: Build an Interview Schedule

Show upcoming interviews in a calendar/agenda format.

## User story
As an employer, I need to see interviews that are scheduled in the future so that I can understand what my day/week looks like and I don’t miss any interviews.

## Directions
Build an application to create, manage, and display interviews.

### Front End
 * Show agenda of interviews by day
 * Group interviews by date, time asc
 * Basic CrUD interview components

### Back End
 * Create models for Candidates and Interviews. 
   * Interviews should have 1 candidate, a scheduled time, and a location name.
   * Candidates should have a name and email.
 * Build a GraphQL Query for Interviews
 * Paginate for results via Relay spec
 * Build basic CrUD mutations for Interview
