# Use Node for build
FROM node:18

# Set working dir
WORKDIR /app

# Copy dependency files
COPY package*.json ./

# Install
RUN npm install

# Copy rest
COPY . .

# Build (uncomment if your frontend has a build step)
# RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
