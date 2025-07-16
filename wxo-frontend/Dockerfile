# 1. Use official Node.js image as the build environment
FROM node:20 as build

# 2. Set working directory
WORKDIR /app

# 3. Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# 4. Copy the rest of the source code
COPY . .

# 5. Build the React app for production
RUN npm run build

# 6. Use a lightweight web server (Nginx) to serve the static files
FROM nginx:alpine

# 7. Copy built files to Nginx's web root
COPY --from=build /app/build /usr/share/nginx/html

# 8. Expose port 80
EXPOSE 80

# 9. Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
