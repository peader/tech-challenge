## Description
This repo attempts to setup a kubernetes cluster, deploy an application comprised of a backend (python flask) and frontend (nginx) service to said cluster using a combination of continuous integration, helm and githubt actions.

Everything runs locally on the host machine.

## Arcithecture
### Dataflow
``` mermaid
graph LR
    classDef Env fill:#f9f,stroke:#333,stroke-width:4px;
    classDef App fill:#ccf,stroke:#f66,stroke-width:4px;
    classDef Service fill:#fcc,stroke:#966,stroke-width:4px;

    dev[Env;dev]
    stg[Env;stg]
    prod[Env;prod]

    frontend[App;frontend]
    backend[App;backend]

    frontend -->|requests|> nginx[Service;nginx]
    nginx -->|proxy|> backend

    dev -->|http://control-node:30008|> frontend
    stg -->|http://control-node:30009|> frontend
    prod -->|http://control-node:30010|> frontend
```

### Deployment flow
``` mermaid
graph LR
    classDef Step fill:#f9f,stroke:#333,stroke-width:4px;
    classDef Action fill:#ccf,stroke:#f66,stroke-width:4px;

    A[Create Docker Images] -->|with unique version|> B[Push to Local Registry]
    B -->|update helm chart|> C[Deploy Helm Chart]
    C -->|with updated docker version|> D[Moose Facts Application]

    A[Create Docker Images] -->|create frontend image|> E[Frontend Image]
    A[Create Docker Images] -->|create backend image|> F[Backend Image]

    E -->|push to registry|> B[Push to Local Registry]
    F -->|push to registry|> B[Push to Local Registry]

    C -->|deploy|> G[Local Kubernetes Cluster]
    G -->|run|> D[Moose Facts Application]
```

## Hardware
The environment is designed for use on a raspberry pi 5 running the raspbian lite arm64 OS.
The host name of the system is control-node. (Used to connect to the cluster from outside the hosts local network)

## Usage
- Fork the [tech-challenge](https://github.com/peader/tech-challenge) repo.
- Run the setup_environment.sh script at the root of the repo.
- Follow the manual instructions that are printed to the terminal.
    - 1. Copy the content of /etc/rancher/k3s/k3s.yaml
    - 2. Replace the <your-kube-config> string in the secrets/my-custom.secrets file with the copied content
    - 3. Restart the raspberry pi
- Run the command:
    ``` bash
    act --job docker --secret-file=secrets/my-custom.secrets
    ```
- Run the command:
    ``` bash
    act --job deployment-dev --secret-file=secrets/my-custom.secrets
    ```
- Open a browser and navigate to http://control-node:30008. You should see the moose facts website.
- Deploy the staging and production environment with the following commands:
    ``` bash
    act --job deployment-stg --secret-file=secrets/my-custom.secrets
    act --job deployment-prod --secret-file=secrets/my-custom.secrets
    ```
- Navigate to http://control-node:3001 (this is our kuma uptime monitoring service).
- Input your new credentials and login.
- Add three new dashboards. One for dev, stg and production with the urls:
    - http://control-node:30008
    - http://control-node:30009
    - http://control-node:30010

## Making changes
- Simply change either the application/backend/server.py file, for example add a new endpoint or modify and existing endpoint or modify the html file at application/frontend/index.html.
- Commit the changes (needed for updating the image reviosion).
- Run the commands:
    ``` bash
    act --job docker --secret-file=secrets/my-custom.secrets
    act --job deployment-dev --secret-file=secrets/my-custom.secrets
    ```
You should see the changes reflected in the moose facts website at url http://control-node:30008

## Troubleshooting
- If the site is not acting as expected run the command
``` bash
kubectl get pods
```
to get the status of the pods created by the deployment.
- If you need further info on a particular pod run the command:
``` bash
kubectl logs -l app=<frontend or backend>-<environment> --all-containers=true
```

## Other useful commands
```
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
helm uninstall moose-facts-<environment>
```



