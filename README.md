# StarHunt Gh

## About StarHunt Gh

Growing up in Ghana, I played football with friends who were some of the most talented players I'd ever seen. Some could dribble past three defenders without breaking a sweat, while others could score goals from almost anywhere on the pitch. But despite how good they were, no scouts ever came to our neighborhood to watch them play. They never really got the opportunity to show what they could do. Their talent stayed on those dusty local pitches, and that's something I've never forgotten.

That's what inspired me to create StarHunt Gh.

StarHunt Gh is a football scouting platform designed to help talented young footballers in Ghana get noticed. The idea is to give players a place to showcase their abilities and make it easier for scouts and coaches to discover potential talent.

The goal is to allow players to create profiles, share their playing positions, teams, statistics, and links to their best football highlights. Scouts and coaches would be able to search for players based on things like their positions, ages, and regions.

Since many of these players are young, safety is also part of the plan. I want to include features such as scout verification and parental or guardian approval for players under 18, so that young footballers can connect with opportunities more safely.

For me, StarHunt Gh is more than just a coding project. It's something I wish had existed when I was growing up. I hope it can eventually give talented players opportunities they might otherwise miss simply because of where they come from.

## Installation

If you want to try StarHunt Gh on your own computer, here's how to get everything set up.

Before you begin, make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) and [Git](https://git-scm.com/) installed on your computer. Docker helps run the application without having to install and configure everything manually.

### Step 1: Get the project

First, open your terminal and clone the project from GitHub. Then move into the project folder and create your environment file.

```bash
git clone https://github.com/ekoranteng60/starhunt-gh.git
cd starhunt-gh
cp .env.example .env
```

The `.env` file is where you'll keep important settings, such as your database password and secret key.

### Step 2: Set up your environment

Open the `.env` file and replace the example database password and secret key with your own values.

If you don't already have a secret key, you can generate one by running:

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(50))"
```

Copy the generated key and paste it into the appropriate place in your `.env` file. Make sure to keep this information private.

### Step 3: Build the application

Once your environment file is ready, you can build the application using Docker.

```bash
docker-compose build
```

Next, set up the database by running the migrations.

```bash
docker-compose run --rm app python manage.py migrate
```

Finally, create a superuser account so you can log in and manage the application.

```bash
docker-compose run --rm app python manage.py createsuperuser
```

You'll be asked to enter a username, email address, and password. Make sure you remember your login details because you'll need them to access the admin dashboard.

## Getting Started

Now that everything is set up, you're ready to run StarHunt Gh.

Start the application by running:

```bash
docker-compose up
```

Once the application is running, open your browser and visit:

http://localhost:8000/admin

Log in using the superuser account you created during installation.

From the admin dashboard, look for the **Players** section and select **Player profiles**.

Here, you can add new players, view their information, search through existing profiles, and filter players based on their positions and regions.

When you're finished using the application, go back to your terminal and press `Ctrl + C` to stop it.

## Design Documents

The design documents are in [docs/README.md](docs/README.md). They include:

- **User stories:** what players, scouts, and other users should be able to do on the platform.
- **Mis-user stories:** ways someone might misuse the platform and how those risks are addressed.
- **Mockup:** what the platform's interface could look like.
- **Architecture diagrams:** how the different parts of the application are organized and work together.

## License

StarHunt Gh is an open-source project released under the MIT License.

This means others are free to use, modify, and share the code as long as they follow the license terms.

For more information, see the [LICENSE](LICENSE) file.