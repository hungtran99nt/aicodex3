# Architecture Diagram for Quiz Game System

## Overview
This architecture diagram illustrates how different components of the quiz game system interact, including the server, client applications, database, and any external services.

## Architecture Diagram
```mermaid
graph TD
    subgraph Client Applications
        A[User Interface]
    end

    subgraph Server
        B[User Registration Service]
        C[Quiz Creation Service]
        D[Quiz Participation Service]
        E[Notification Service]
        F[Scoring Service]
        G[Leaderboard Service]
        H[Event Bus]
    end

    subgraph Database
        I[(Database)]
    end

    subgraph Monitoring
        J[Monitoring Service]
    end

    subgraph External Services
        K[Email Service]
        L[SMS Service]
    end

    A -->|User Details| B
    A -->|Quiz Details| C
    A -->|User Answers| D

    B -->|UserRegistered Event| H
    C -->|QuizCreated Event| H
    D -->|QuizStarted, QuizAnswered, QuizCompleted Events| H

    H -->|UserRegistered Event| E
    H -->|QuizCreated Event| E
    H -->|QuizAnswered, QuizCompleted Events| F
    H -->|QuizCompleted Event| G

    B -->|Store User Data| I
    C -->|Store Quiz Data| I
    D -->|Update Quiz Progress| I
    F -->|Update Scores| I
    G -->|Update Leaderboards| I

    E -->|Send Notifications| K
    E -->|Send Notifications| L

    J -->|Collect Metrics| B
    J -->|Collect Metrics| C
    J -->|Collect Metrics| D
    J -->|Collect Metrics| E
    J -->|Collect Metrics| F
    J -->|Collect Metrics| G