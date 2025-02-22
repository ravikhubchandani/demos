# Log in to Azure
```
az login
```
```
az acr login --name <acr-name>
For example: az acr login --name ravicontainerimages
```

# Prepare image tag
```
docker tag <local-image-name>:<local-image-version> <acr-name>.azurecr.io/<remote-image-name>:<remote-image-version>
For example: docker tag time-recorder:latest ravicontainerimages.azurecr.io/time-recorder:latest
```

# Push image
```
docker push <acr-name>.azurecr.io/<remote-image-name>:<remote-image-version>
For example: docker push ravicontainerimages.azurecr.io/time-recorder:latest
```

## At this point the image should be available in Azure Portal, assuming everything went well
Also can be checked in console:
```
az acr repository list --name <acr-name> --output table
For example: az acr repository list --name ravicontainerimages --output table
```
