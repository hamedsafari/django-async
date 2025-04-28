FROM node:22.8-slim
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci
COPY . .
EXPOSE 3000
RUN npm run build
CMD HOSTNAME="0.0.0.0" npm run dev