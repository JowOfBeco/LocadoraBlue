-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema locadora
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema locadora
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `locadora` DEFAULT CHARACTER SET utf8 ;
USE `locadora` ;

-- -----------------------------------------------------
-- Table `locadora`.`diretores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `locadora`.`diretores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome_completo` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `locadora`.`generos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `locadora`.`generos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `locadora`.`filmes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `locadora`.`filmes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(255) NULL,
  `ano` INT NULL,
  `classificacao` INT NULL,
  `preco` DECIMAL(5,2) NULL,
  `diretores_id` INT NOT NULL,
  `generos_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_filmes_diretores_idx` (`diretores_id` ASC) VISIBLE,
  INDEX `fk_filmes_generos1_idx` (`generos_id` ASC) VISIBLE,
  CONSTRAINT `fk_filmes_diretores`
    FOREIGN KEY (`diretores_id`)
    REFERENCES `locadora`.`diretores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_filmes_generos1`
    FOREIGN KEY (`generos_id`)
    REFERENCES `locadora`.`generos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `locadora`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `locadora`.`usuarios` (
  `id` INT NOT NULL,
  `nome_completo` VARCHAR(255) NULL,
  `CPF` CHAR(14) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `locadora`.`locacoes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `locadora`.`locacoes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `data_inicio` DATETIME NULL,
  `data_fim` DATETIME NULL,
  `filmes_id` INT NOT NULL,
  `usuarios_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_locacoes_filmes1_idx` (`filmes_id` ASC) VISIBLE,
  INDEX `fk_locacoes_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_locacoes_filmes1`
    FOREIGN KEY (`filmes_id`)
    REFERENCES `locadora`.`filmes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_locacoes_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `locadora`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `locadora`.`pagamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `locadora`.`pagamento` (
  `id` INT NOT NULL,
  `tipo` ENUM("dredito", "crebito", "paypal") NULL,
  `status` ENUM("aprovado", "em analise", "reprovado") NULL,
  `codigo_pagamento` VARCHAR(255) NULL,
  `valor` DECIMAL(9,2) NULL,
  `data` DATETIME NULL,
  `locacoes_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pagamento_locacoes1_idx` (`locacoes_id` ASC) VISIBLE,
  CONSTRAINT `fk_pagamento_locacoes1`
    FOREIGN KEY (`locacoes_id`)
    REFERENCES `locadora`.`locacoes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
