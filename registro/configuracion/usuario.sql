-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema datos_clientes
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema datos_clientes
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `datos_clientes` DEFAULT CHARACTER SET utf8 ;
USE `datos_clientes` ;

-- -----------------------------------------------------
-- Table `datos_clientes`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `datos_clientes`.`usuario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(156) NULL,
  `apellido` VARCHAR(156) NULL,
  `email` VARCHAR(156) NULL,
  `password` VARCHAR(156) NULL,
  `creado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `actualizado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
