/* CREATE DATABASE gerenciador_de_tarefas; */
USE gerenciador_de_tarefas;
CREATE TABLE tarefas(
id_tarefas INT AUTO_INCREMENT PRIMARY KEY,
descricao VARCHAR(255) NOT NULL,
data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
status VARCHAR(50) DEFAULT 'pendente')