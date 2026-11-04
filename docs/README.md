# StarHunt Gh Design Documents

## User Stories

### User Story-1: Create a player profile
As a **young football player**, I want to **build a profile with my personal data and football background** so I can **be recognized by scouts and coaches**.

**Acceptance criteria**
- A player can register with a username and password.
- The profile form needs a full name, date of birth, position, region, and preferred foot.
- Position and region are picked from fixed lists (10 positions, 16 Ghana regions).
- Town, current team, height, weight, goals, assists, and number of matches played can also be added.
- After saving, the player can access and edit their own profile.

### User Story-2: Share highlight videos
As a **young football player**, I want to **add a link to my highlight video** so I can **show scouts what I can do on the pitch**.

**Acceptance criteria**
- A player can add a highlight link to their profile.
- Only YouTube links (youtube.com or youtu.be) are accepted.
- Any other link is declined with the message "Please enter a valid YouTube link for your highlights."

### User Story-3: Search for players
As a **scout**, I want to **look for players by region and position** so I can **find talent that fits my team's needs**.

**Acceptance criteria**
- A scout can filter players by any of the 10 positions.
- A scout can filter players by any of the 16 regions of Ghana.
- Both filters can be used together (e.g. strikers in Ashanti).
- Results will show each player's name, position, region, and age.

### User Story-4: Approve a minor's profile
As a **parent or guardian**, I want to **approve my child's profile before scouts can see it** so I can **make sure my child has protection**.

**Acceptance criteria**
- Players below the age of 18 start with their profile marked as not approved.
- Profiles that are not approved are not visible in scout searches.
- Once approved, the profile appears in scout searches.

### User Story-5: Verify scouts
As an **administrator**, I want to **verify that each scout is authorized before they can search for players** so I can **protect players from fake agents and frauds**.

**Acceptance criteria**
- New scout accounts start as unverified.
- Unverified scouts cannot search or view player profiles.
- Only an administrator can mark a scout as verified.

### User Story-6: Manage the platform
As an **administrator**, I want to **review, edit, and remove player and scout accounts** so I can **keep the platform legitimate and safe**.

**Acceptance criteria**
- Only administrators can access the admin panel.
- An administrator can search and filter player profiles.
- An administrator can deactivate any account that breaks the rules and regulations.