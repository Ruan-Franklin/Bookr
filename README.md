# Bookr

Bookr is a modern full-stack scheduling and booking platform designed for service providers such as barbershops, clinics, and sports courts.

## Overview

Bookr helps businesses manage appointments, showcase their services, and provide a simple booking experience for clients. The platform is designed to streamline scheduling, improve customer experience, and make service management more efficient for professionals and organizations.

## Why Bookr?

Many service-based businesses still rely on manual scheduling, phone calls, or disconnected tools. Bookr aims to centralize the booking process by combining:

- service catalog management
- professional profiles
- appointment scheduling
- user accounts and authentication
- reviews and customer feedback

## Main Features

- Service provider profiles and availability management
- Online appointment booking for customers
- Service listings with pricing, duration, and images
- User authentication and profile management
- Professional and client roles
- Review and rating system for services
- Appointment status tracking
- Clean, scalable domain model for future expansion

## Core Domain Model

The application is organized around a set of core entities represented in the class diagram:

- User: represents a customer or business account with personal information, authentication, and profile details.
- Professional: represents a service provider with specialty, bio, and booking-related attributes.
- Service: represents a service offering with description, duration, price, and associated image.
- Appointment: represents a scheduled booking between a client and a professional, including start time and status.
- Review: stores customer feedback and ratings for a service or professional.
- BaseModel: shared model superclass containing common metadata such as timestamps and ownership information.

## Business Flow

1. A user creates an account and manages their profile.
2. A professional is registered with their specialties and available services.
3. Customers browse services and book an appointment.
4. The appointment is tracked through its lifecycle.
5. Clients can leave reviews and ratings after the service.

## Project Goals

Bookr is intended to be:

- practical and easy to use
- flexible enough for different service industries
- scalable for future features such as payments, calendars, notifications, and admin dashboards
- built on a solid domain model that supports maintainable development

## Roadmap

- Define requirements and user flows
- Build the backend APIs and database model
- Implement authentication and authorization
- Develop the frontend booking experience
- Add review, scheduling, and admin features
- Improve performance, validation, and deployment readiness

## Status

This project is currently in the design and planning phase, with the class diagram serving as the foundation for the system architecture and domain structure.

## Documentation

- [Requirements](docs/requirements.md)

## License

This project is licensed under the MIT License. See the LICENSE file for details.
