# Monitoring the Work
We use the idea of velocity as an indicator of the progress of work - in the traditional approach, we would have used many formulae, reports and tools.

## Status of the iteration
Recall that in agile, the scope is determined by the schedule and budget, not the other way around. For an iteration, determining the completion status is as simple as looking at the Kanban board a.k.a. the task panel.

The tasks on the Kanban board each have an estimated time required for completion. We can tell iteration progress by summing up the number of hours for the tasks that are currently moving across the board. It is also possible for us to consider the time elapsed for each tasks but because we discourage having really long tasks (therefore splitting them up into smaller ones), it is highly unlikely that keeping track of the number of hours spent on each tasks might turn out to be a wasteful practice.

Having more tasks on the left side of the board means that the work in the iteration is still in its initial stages - this is fine in the iteration's beginning but we should be concerned if the cards are not moving to the right as time passes.

Another way to determine the state of work is to look at the burndown diagram. We want the real line to be below the ideal line - the iteration is ahead of where it is expected to be.

## Status of an agile project
We can determine if the project is on track by extrapolating from the burndown (the graph of story points remaining versus time elapsed) a function that indicates the velocity of the project forward into the future. In this way, we predict where we expect the project to be, given the current rate at which the work team is moving requirements into the fulfilled state.

The ideal line on the burndown has a negative gradient and cuts the time axis where we expect the project should end. We will finish ahead of time as long as the real line remains below the ideal. The gradient of the real line (usually negative for a progressing project) on the burndown indicates to us the rate at which we are actually completing tasks. When there is a positive gradient for the real line, it means that there is some increase in the total number of story points left to be completed.

Agile management software usually generate the burndown automatically. There are also burnup diagrams which behave in a similar manner but have an ideal line that ascends to the total number of points instead.

We calculate the velocity by finding the average number of story points completed in each iteration.
