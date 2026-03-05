# Rate My Creamtea

A user-friendly community site for people of all ages to document and share their experiences of cream tea.

## Deployment

Deployed link:
This project is hosted on heroku, with cloudinary image hosting, postgreSQL db and gunicon runtime engine.

To configure this project for local use you will need to add the following to an env file:

- Database URL
- Cloudinary URL
- App Secret key

Python dependencies are listed in requirement.txt

## Technologies

HTML, CSS5, Bootstrap 5.3.
Django, allauth, gunicorn, summernote, whitenoise.
Cloudinary for image hosting
Heroku for deployment.

## User stories

- **#1 Upload image** - As a logged-in user, I can upload an image with my cream tea post so that others can see what it looked like.
- **#2 Browse posts** - As a site user, I can browse posts and comments so that I can view content.
- **#3 Admin post control** - As admin, I can add and remove posts from the admin panel, so that I can efficiently use my site.
- **#4 Admin comment control** - As admin, I can approve comments so that I can control content.
- **#5 Edit/delete review** - As a logged-in user, I can edit or delete my own comments so that I can correct mistakes or update information.
- **#6 Edit/delete post** -As a logged-in user, I can edit or delete my own post so that I can correct mistakes or update information.
- **#7 Rating** - As a logged-in user, I can give a cream tea a rating and leave a comment so that others can quickly judge its quality.
- **#8 Add posts** - As a logged in user, I can add posts that I can share my cream tea experience with others.
- **#9 Comment on posts** - As a logged in user, I can comment on posts so that I can review cream teas.

## Features

From these user stories we derived features:

- List view for posts.
- Add a new post with image and rating for logged in users.
- Edit post.
- Add/Edit/Delete comments.
- Admin panel for site staff moderation control.

## UX Design

Our primary focus in implementing these features for our user group was simple and navigable design.

<img width="779" height="1122" alt="image" src="https://github.com/user-attachments/assets/3b024796-e1f2-4fd8-b5f9-446703b33dde" />

From our wireframe, we were able to implement a simple, clean and responsive design.
<img width="1693" height="900" alt="image" src="https://github.com/user-attachments/assets/745d9fa8-ad34-42e3-8308-d64f11341405" />

With a bright colourscheme, we hoped to invoke the feeling of cream teas, and helped ensure that all areas meet WCAG colour contrast ratios.
## Testing

HTML Validation with W3C validator
Accessibility testing with WaveAIM
Automated testing was beyond the scope of this project.

## Agile development approach

Due to the short development timeframe, we elected to conduct each project day as a sprint with daily scrum to assign tasks and ensure a common understanding of task priority.


## AI usage

AI usage was very light in this project due to time constraints and small project scope.
AI was used for debugging, text pack creation and project css library creation.
To aid development under short time frames, after creating the initial project and defining requirements, AI was used to create a css library. This gave consistent styling for elements and repeatable classes to use throughout development, without having to rely solely on bootstrap or custom css.
