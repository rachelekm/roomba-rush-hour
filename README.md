# Roomba Rush Hour

A breakable toy project testing an unlikely, unnecessary scenario: how long will it take a roomba to sweep a given Philadelphia sidewalk.

### Requirements

-   Vagrant 2.2+
-   VirtualBox 6.0+
-   Ansible 2.9+

### Getting Started

Install the application and all required dependencies.

```sh
./scripts/setup
```

#### Development

Rebuild Docker images and run application.

```sh
vagrant ssh
./scripts/server
```

### Ports

| Service | Port                            |
| ------- | ------------------------------- |
| Django  | [`8080`](http://localhost:8080) |

### Testing

```
./scripts/test
```

### Scripts

| Name      | Description                                           |
| --------- | ----------------------------------------------------- |
| `clean`   | Free disk space by cleaning up dangling Docker images |
| `console` | Run interactive shell inside application container    |
| `lint`    | Lint source code                                      |
| `server`  | Run Docker Compose services                           |
| `setup`   | Provision Vagrant VM and run `update`                 |
| `test`    | Run unit tests                                        |
| `update`  | Build Docker images                                   |
