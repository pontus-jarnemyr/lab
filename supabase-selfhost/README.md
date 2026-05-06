# Supabase

Minimal setup for self-hosting Supabase using Docker compose. 

## Basic usage

| Action    | Command                                                                       |
| ---       | ---                                                                           |
| Start     | `docker compose -f docker-compose.yml`                                        |
| Stop      | `docker compose down`                                                         |
| Destroy   | `docker compose down -f docker-compose.yaml down --volumes --remove-orphans`  |
| Reset     | `./reset.sh`                                                                  |
