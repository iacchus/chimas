### Roles (User roles)

#### admins

`admins` role is a group of users which have complete rights inside the app.

#### moderators 

`moderators` role is a role with [board name] as title, and which give rights to managing boards

maybe title will prefixed with be boardmods\_\<board title\>

#### useronly

`useronly` is a role which only the own user can perform, for example, editing/deleting it's own posts.

These should be well implemented, for example, should we allow admins to edit users posts? etc.

#### registered

`registered` users is a role which only registered users can perform, for example, posting on topics.

#### guests or anonymous

`guests` or `anon` is a role which all non-registered users can perform. We should not include registered ones in this, because we may want to distinguish between them, for example, so we can show a message only for non-registered users.

### Global and Custom roles

#### Global Roles

* admins
* anonymous
* registered

#### Custom roles

*(provided by / roles)*

Boards

* moderators

Posts

* author / owner

Users

* owner
