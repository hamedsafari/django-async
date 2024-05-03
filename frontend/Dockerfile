FROM node:18-alpine
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci
COPY . .
EXPOSE 3000
CMD HOSTNAME="0.0.0.0" npm run dev