# Web application demos

## Social Networking site

A Twitter-like social network website for making posts and following users.

This project is deployed on Heroku (please have patience since the instance is likely sleeping but will wake up after a few seconds): <a href="https://farnellg-social-network.herokuapp.com/">https://farnellg-social-network.herokuapp.com/</a>

A screencast of the project can be found here: <a href="https://youtu.be/mnw06wUITk8">https://youtu.be/mnw06wUITk8</a>

You can log in to the Heroku app above with this account that is already entered by default. No registration is required (although you can register):

* User: **guest**
* Password: **123**

Some of the technologies I used when building this demo application:

* Javascript (vanilla, not a framework) with AJAX
* APIs in Python that return a JSON response
* Visual Studio Code
* Django web framework.  I used Django's Paginator class to paginate the postings and stylized the pagination with Bootstrap.
* Git.
* HTML
* CSS
* Heroku hosting

-----------
**Project overview**

This demo application completed the requirements below using JavaScript, Django/Python, HTML, and CSS:

* **New Post**: Users who are signed in should be able to write a new text-based post by filling in text into a text area and then clicking a button to submit the post.
    * The screenshot at the top of this specification shows the “New Post” box at the top of the “All Posts” page. You may choose to do this as well, or you may make the “New Post” feature a separate page.

* **All Posts**: The “All Posts” link in the navigation bar should take the user to a page where they can see all posts from all users, with the most recent posts first.
    * Each post should include the username of the poster, the post content itself, the date and time at which the post was made, and the number of “likes” the post has (this will be 0 for all posts until you implement the ability to “like” a post later).

* **Profile Page**: Clicking on a username should load that user’s profile page. This page should:
    * Display the number of followers the user has, as well as the number of people that the user follows.
    * Display all of the posts for that user, in reverse chronological order.
    * For any other user who is signed in, this page should also display a “Follow” or “Unfollow” button that will let the current user toggle whether or not they are * following this user’s posts. Note that this only applies to any “other” user: a user should not be able to follow themselves.

* **Following**: The “Following” link in the navigation bar should take the user to a page where they see all posts made by users that the current user follows.
    * This page should behave just as the “All Posts” page does, just with a more limited set of posts.
    * This page should only be available to users who are signed in.

* **Pagination**: On any page that displays posts, posts should only be displayed 10 on a page. If there are more than ten posts, a “Next” button should appear to take the user to the next page of posts (which should be older than the current page of posts). If not on the first page, a “Previous” button should appear to take the user to the previous page of posts as well.
    * See the Hints section for some suggestions on how to implement this.

* **Edit Post**: Users should be able to click an “Edit” button or link on any of their own posts to edit that post.
    * When a user clicks “Edit” for one of their own posts, the content of their post should be replaced with a textarea where the user can edit the content of their post.
    * The user should then be able to “Save” the edited post. Using JavaScript, you should be able to achieve this without requiring a reload of the entire page.
    * For security, ensure that your application is designed such that it is not possible for a user, via any route, to edit another user’s posts.

* **“Like” and “Unlike”**: Users should be able to click a button or link on any post to toggle whether or not they “like” that post.
    * Using JavaScript, you should asynchronously let the server know to update the like count (as via a call to fetch) and then update the post’s like count displayed on the page, without requiring a reload of the entire page.

-----------

## e-Commerce website

This simple app is an eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on listings, and add listings to a “watchlist.”

This project is deployed on Heroku (please have patience since the instance is likely sleeping but will wake up after a few seconds): <a href="https://python-django-commerce.herokuapp.com/">https://python-django-commerce.herokuapp.com/</a>

A screencast of the project can be found here: <a href="https://youtu.be/6WfF_JHMtnU">https://youtu.be/6WfF_JHMtnU</a>

You can log in to the Heroku app above with this account that is already entered by default. No registration is required (although you can register):

* username: **guest**
* password: **123**

Some of the technologies I used when building this demo application:

* Visual Studio Code
* Django web framework
* Python
* Git
* HTML
* CSS
* Heroku hosting

-----------
 **Project overview**

* **Models**: Application contains more than three models in addition to the User model: one for auction listings, one for bids, and one for comments made on auction listings.  See the **models.py** file for more information.

* **Create Listing**: Users can visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users can also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).

* **Active Listings Page**: The default route of the web application lets users view all of the currently active auction listings. For each active listing, this page displays (at minimum) the title, description, current price, and photo (if one exists for the listing).

* **Listing Page**: Clicking on a listing takes users to a page specific to that listing. On that page, users can view all details about the listing, including the current price for the listing.
    * If the user is signed in, the user should be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user should be able to remove it.
    * If the user is signed in, the user should be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user should be presented with an error.
    * If the user is signed in and is the one who created the listing, the user can “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.
    * If a user is signed in on a closed listing page, and the user has won that auction, the page should say so.
    * Users who are signed in can add comments to the listing page. The listing page displays all comments that have been made on the listing.
* **Watchlist**: Users who are signed in can visit a Watchlist page which displays all of the listings that a user has added to their watchlist. Clicking on any of those listings takes the user to that listing’s page.
* **Categories**: Users can visit a page that displays a list of all listing categories. Clicking on the name of any category takes the user to a page that displays all of the active listings in that category.
* **Django Admin Interface**: Via the Django admin interface, as a site administrator you can view, add, edit, and delete any listings, comments, and bids made on the site.

-----------

## Single-page Javascript web application

This project is a single-page Javascript application.  It is a mock email client application that makes API calls to compose, send and archive/unarchive email.  This project utilizes pre-built Python APIs with GET, POST and PUT requests in Javascript.  AJAX is used to fetch data from the server.  Javascript is used to display/hide information and manipulate the DOM for the various views in the app.

You can use these credentials for the application:
User email: **guest@example.com**
Password: **123**

You can also use these email addresses with the same password of "123" without the quotes: **foo@example.com**, **bar@example.com**, **baz@example.com**.

You can also register and create your own credentials.

This project is deployed on Heroku (please have patience since the instance is likely sleeping but will wake up after a few seconds): <a href="https://mail-client-gfarnell.herokuapp.com/">https://mail-client-gfarnell.herokuapp.com/</a>

A screencast of the project can be found here: <a href="https://youtu.be/V2s00sozPkU">https://youtu.be/V2s00sozPkU</a>

You can log in to the Heroku app above with this account that is already entered by default. No registration is required (although you can register):

* Email: **guest**
* Password: **123**

Some of the technologies I used when building this demo application:

* Javascript (vanilla, not a framework)
* Visual Studio Code
* Django web framework
* Git
* HTML
* CSS
* Heroku hosting

-----------
**Project overview**

Using JavaScript, HTML, and CSS, complete the implementation of your single-page-app email client inside of inbox.js (and not additional or other files; for grading purposes, we’re only going to be considering inbox.js!). You must fulfill the following requirements:

* **Send Mail**: When a user submits the email composition form, add JavaScript code to actually send the email.
    * You’ll likely want to make a POST request to /emails, passing in values for recipients, subject, and body.
    * Once the email has been sent, load the user’s sent mailbox.

* **Mailbox**: When a user visits their Inbox, Sent mailbox, or Archive, load the appropriate mailbox.
    * You’ll likely want to make a GET request to /emails/<mailbox> to request the emails for a particular mailbox.
    * When a mailbox is visited, the application should first query the API for the latest emails in that mailbox.
    * When a mailbox is visited, the name of the mailbox should appear at the top of the page (this part is done for you).
    * Each email should then be rendered in its own box (e.g. as a <div> with a border) that displays who the email is from, what the subject line is, and the timestamp of the email.
    * If the email is unread, it should appear with a white background. If the email has been read, it should appear with a gray background.

* **View Email**: When a user clicks on an email, the user should be taken to a view where they see the content of that email.
    * You’ll likely want to make a GET request to /emails/<email_id> to request the email.
    * Your application should show the email’s sender, recipients, subject, timestamp, and body.
    * You’ll likely want to add an additional div to inbox.html (in addition to emails-view and compose-view) for displaying the email. Be sure to update your code to hide and show the right views when navigation options are clicked.
    * Once the email has been clicked on, you should mark the email as read. Recall that you can send a PUT request to /emails/<email_id> to update whether an email is read or not.

* **Archive and Unarchive**: Allow users to archive and unarchive emails that they have received.
    * When viewing an Inbox email, the user should be presented with a button that lets them archive the email. When viewing an Archive email, the user should be presented with a button that lets them unarchive the email. This requirement does not apply to emails in the Sent mailbox.
    * Recall that you can send a PUT request to /emails/<email_id> to mark an email as archived or unarchived.
    * Once an email has been archived or unarchived, load the user’s inbox.

* **Reply**: Allow users to reply to an email.
    * When viewing an email, the user should be presented with a “Reply” button that lets them reply to the email.
    * When the user clicks the “Reply” button, they should be taken to the email composition form.
    * Pre-fill the composition form with the recipient field set to whoever sent the original email.
    * Pre-fill the subject line. If the original email had a subject line of foo, the new subject line should be Re: foo. (If the subject line already begins with Re: , no need to add it again.)
    * Pre-fill the body of the email with a line like "On Jan 1 2020, 12:00 AM foo@example.com wrote:" followed by the original text of the email.

-----------

## Wiki markdown converter

This application allows users to create wiki topics/entries in Markdown format and save the entry in to the Django SQLITE3 database.  When viewing topics, Markdown content is retrieved from the database and displayed in the browser in HTML format.  The __python-markdown2__ package is used to convert the markdown to HTML and vice-versa.

This project is deployed on Heroku (have patience since the instance is likely sleeping): <a href="https://wiki-markdown-gfarnell.herokuapp.com/">https://wiki-markdown-gfarnell.herokuapp.com/</a>

A screencast of the project can be found here: <a href="https://youtu.be/XYzJSfeYuJI">https://youtu.be/XYzJSfeYuJI</a>

Some of the technologies I used when building the wiki app:

* Visual Studio Code
* Django web framework
* Python
* Git
* HTML
* CSS

-----------
**Project overview**

* **Entry Page**: Visiting */wiki/TITLE*, where **TITLE** is the title of an encyclopedia entry, will render a page that displays the contents of that encyclopedia entry.
    * The view gets the contents of the encyclopedia entry by calling the appropriate utility function.
    * If an entry is requested that does not exist, the user is presented with an error page indicating that their requested page was not found.
    * If the entry does exist, the user is presented with a page that displays the content of the entry. The title of the page includes the name of the entry.

* **Index Page**: The *index.html* lists the names of all pages in the encyclopedia and the user can click on any entry name to be taken directly to that entry page.

* **Search**: The user can type a query into the search box in the sidebar to search for an encyclopedia entry.
    * If the query matches the name of an encyclopedia entry, the user is redirected to that entry’s page.
    * If the query does not match the name of an encyclopedia entry, the user is instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were *ytho*, then Python should appear in the search results.
    * Clicking on any of the entry names on the search results page takes the user to that entry’s page.

* **New Page**: Clicking “Create New Page” in the sidebar takes the user to a page where they can create a new encyclopedia entry.
    * Users can enter a title for the page and, in a textarea, can enter the Markdown content for the page.
    * Users can click a button to save their new page.
    * When the page is saved, if an encyclopedia entry already exists with the provided title, the user is presented with an error message.
    Otherwise, the encyclopedia entry is saved to disk, and the user is taken to the new entry’s page.

* **Edit Page**: On each entry page, the user can click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
    * The textarea is pre-populated with the existing Markdown content of the page. (i.e., the existing is the initial value of the textarea).
    * The user can click a button to save the changes made to the entry.
    * Once the entry is saved, the user is redirected back to that entry’s page.

* **Random Page**: Clicking “Random Page” in the sidebar takes the user to a random encyclopedia entry displayed in HTML format that the user can then edit.

* **Markdown to HTML Conversion**: On each entry’s page, any Markdown content in the entry file is converted to HTML before being displayed to the user. The python-markdown2 package is used to perform this conversion.
