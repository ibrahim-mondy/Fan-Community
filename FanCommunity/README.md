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


# User Endpoints
# signin
# http://localhost:8000/api/auth/signup/
{
  "username": "EbrahimMondy",
  "password": "Ibrahim&88888"
}

# Add Movies
# http://localhost:8000/api/movies/
{
    "title": "Scarface",
    "description": "A crime film about the rise and fall of a Cuban immigrant in Miami's criminal underworld.",
    "release_date": "1983-12-09",
    "genre": "Crime/Drama"
}


# Add Teame
# http://localhost:8000/api/teams/
{
    "name": "Barcelona",
    "country": "Spain",
    "founded_year": 1899
}

# logout
# http://localhost:8000/api/auth/logout/
