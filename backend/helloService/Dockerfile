# Use official Node.js LTS version
FROM node:18

# Set working directory inside container
WORKDIR /app

# Copy only package.json and package-lock.json first
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy rest of the app
COPY . .

# Expose port if needed (adjust if your app runs on different port)
EXPOSE 5000

# Command to run the app
CMD ["node", "index.js"]
