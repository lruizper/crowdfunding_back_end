# crowdfunding_back_end
She Codes Crowdfunding back end project using DFR

To populate projects DB use fixtures provided in projects/fixtures/my_fixtures_LRP.json


Project Requirements
[ ] Be separated into two distinct projects: an API built using the Django RestFramework and a website built using React.
[ ] Have a cool name.
[ ] Have a clear target audience.
[ ] Have user accounts. A user should have at least the following attributes:
    [ ] Username
    [ ] Email address
    [ ] Password
[ ] Ability to create a “project” to be crowdfunded which will include at least the following attributes:
    [ ] Title
    [ ] Owner (a user)
    [ ] Description
    [ ] Image
    [ ] Target amount to fundraise
    [ ] Whether it is currently open to accepting new supporters or not
    [ ] When the project was created
[ ] Ability to “pledge” to a project. A pledge should include at least the followingattributes:
    [ ] An amount
    [ ] The project the pledge is for
    [ ] The supporter/user (i.e. who created the pledge)
    [ ] Whether the pledge is anonymous or not
    [ ] A comment to go along with the pledge
[ ] Implement suitable update/delete functionality, e.g. should a project owner be allowed to update a project description?
[ ] Implement suitable permissions, e.g. who is allowed to delete a pledge?
[ ] Return the relevant status codes for both successful and unsuccessful requests to the API.
[ ] Handle failed requests gracefully (e.g. you should have a custom 404 pagerather than the default error page).
[ ] Use Token Authentication.
[ ] Implement responsive design.



[ ] A link to the deployed project.
[ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
[ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
[ ] A screenshot of Insomnia, demonstrating a token being returned.
[ ] Step by step instructions for how to register a new user and create a newproject (i.e. endpoints and body data).
[ ] Your refined API specification and Database Schema.