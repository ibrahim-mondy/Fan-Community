<!-- #  Fan Community -->

<!-- **Fan Community**  -->
is a platform that brings together movie and football fans in one place.  
It allows users to create accounts, share posts, comment, like, and interact with other fans while exploring movies and football teams they love.

---

<!-- ##  **About the Project** -->

This project was built to practice and demonstrate full-stack backend development with Django and Django REST Framework (DRF).  
The goal is to create a social-style platform that is simple but scalable, focusing on clean APIs, authentication, and role-based permissions.

---

<!-- ##  **Features** -->

<!-- - **Authentication System** -->
  - User registration and login
  - Token-based authentication (DRF TokenAuth)
  - Role management: `Admin`, `Member`

<!-- - **Movie & Football Database** -->
  - Browse available movies and football teams
  - Easily extendable for future data integrations

<!-- - **Community Interaction** -->
  - Create posts about movies or football teams
  - Comment on posts
  - Like/unlike posts

<!-- - **Admin Controls** -->
  - Admin users can manage all posts, comments, and users

<!-- - **Seed Script** -->
  - Preloads sample users, movies, and teams for quick testing

---
 <!-- ##  **Challenges Faced** - -->

- Understanding and implementing 
<!-- **role-based permissions** -->
 for different user types.  
- Designing clean and scalable models to handle movies, teams, posts, comments, and likes.  
- Managing token-based authentication and testing endpoints in Postman.  
- Debugging migration issues during early development.  
- Ensuring the project is ready for future enhancements like search and notifications.

---

 <!-- **How to Run the Project** -->

<!-- ### 1. Clone the Repository -->
```bash
git clone https://github.com/ibrahim-mondy/Fan-Community.git
cd Fan-Community


# Test in video
# signin
# http://localhost:8000/api/auth/signup/
{
  "username": "ibrahim",
  "password": "ibrahim88888"
}

# logout
# http://localhost:8000/api/auth/logout/
Authorization: Token abcd1234token

Token 4411490afe46df610ddaa5cb9fc0b203313f14ed
