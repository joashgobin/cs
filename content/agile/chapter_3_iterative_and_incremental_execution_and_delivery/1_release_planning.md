# Release planning
After completing the project roadmap, we must focus on planning the releases of the project. Release planning involves dividing larger requirements in order to fit a release schedule/delivery plan.

Suppose that the expected work capacity for a iteration is 12 story points. In the case of a requirement's story points exceeding this number, we split the requirement into smaller requirements such that the number of story points of the resulting requirements fit into an iteration.

For example, in the case of us using MoSCoW to prioritize requirements in the stack, we may have 5 Must requirements each with 8 points and 10 Should requirements each having 2 points. For every iteration, we can complete a Must requirement and 2 Should requirements.

## Backlog, roadmap and release plan integration
The roadmap is a guide for the project. The release plan is the execution of this guide. The backlog is the strategy, to cover the work required (in the next few iterations) to deliver the next upcoming release, expressed in terms of requirements.

A roadmap with 16 iterations may have 4 releases, each having 5 requirements. At any point in time, the backlog will have at most 5 requirements.

As the project progresses, the requirements can change and we adjust the release plan in order to match these changes.

## Best practices
The priority of the requirements in the release plan is reflective of what the business finds most valuable at the moment.

When deciding on the which stories to implement first, the team must consider:
- We cannot implement a dependent requirement prior to implementing the prerequisite requirement
- There may be external restrictions such as third party actions and tool required to complete specific requirements
- The neighbouring requirements necessary to complete the story

We can manage risk by placing the riskier stories first.


