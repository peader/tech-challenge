# Use the official .NET 8.0 SDK image as the base
FROM mcr.microsoft.com/dotnet/sdk:8.0

# Set the working directory to /app
WORKDIR /app

# Copy the project files into the container
COPY *.csproj ./

# Restore NuGet packages
RUN dotnet restore

# Copy the rest of the application code into the container
COPY . .

# Build the application
RUN dotnet build -c Release

# Publish the application
RUN dotnet publish -c Release -o /app/publish

# Expose the port the application will run on
EXPOSE 5000

# Set the entry point to run the application
ENTRYPOINT ["dotnet", "/app/publish/backendnetcore.dll"]