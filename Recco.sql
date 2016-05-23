-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema Movie_Recco
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Movie_Recco
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Movie_Recco` ;
USE `Movie_Recco` ;

-- -----------------------------------------------------
-- Table `Movie_Recco`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Movie_Recco`.`users` (
  `idusers` INT NOT NULL AUTO_INCREMENT,
  `age` INT NULL,
  `gender` VARCHAR(45) NULL,
  `occupation` VARCHAR(45) NULL,
  `zip` INT NULL,
  `name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`idusers`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Movie_Recco`.`movies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Movie_Recco`.`movies` (
  `idmovies` INT NOT NULL AUTO_INCREMENT,
  `movie_tile` VARCHAR(45) NULL,
  `video_release_date` DATETIME NULL,
  `imdb_url` VARCHAR(255) NULL,
  `unknown` VARCHAR(45) NULL,
  `action` VARCHAR(45) NULL,
  `adventure` VARCHAR(45) NULL,
  `animation` VARCHAR(45) NULL,
  `children` VARCHAR(45) NULL,
  `comedy` VARCHAR(45) NULL,
  `crime` VARCHAR(45) NULL,
  `documentary` VARCHAR(45) NULL,
  `drama` VARCHAR(45) NULL,
  `fantasy` VARCHAR(45) NULL,
  `film_noir` VARCHAR(45) NULL,
  `horror` VARCHAR(45) NULL,
  `musical` VARCHAR(45) NULL,
  `history` VARCHAR(45) NULL,
  `romance` VARCHAR(45) NULL,
  `sci-fi` VARCHAR(45) NULL,
  `thriller` VARCHAR(45) NULL,
  `war` VARCHAR(45) NULL,
  `western` VARCHAR(45) NULL,
  PRIMARY KEY (`idmovies`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Movie_Recco`.`ratings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Movie_Recco`.`ratings` (
  `idratings` INT NOT NULL,
  `user_id` INT NOT NULL,
  `movie_id` INT NOT NULL,
  `timestamp` DATETIME NULL,
  PRIMARY KEY (`idratings`),
  INDEX `fk_ratings_users_idx` (`user_id` ASC),
  INDEX `fk_ratings_movies1_idx` (`movie_id` ASC),
  CONSTRAINT `fk_ratings_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `Movie_Recco`.`users` (`idusers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ratings_movies1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `Movie_Recco`.`movies` (`idmovies`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Movie_Recco`.`friends`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Movie_Recco`.`friends` (
  `idfriends` INT NOT NULL,
  `friend_number` VARCHAR(45) NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`idfriends`),
  INDEX `fk_friends_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_friends_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `Movie_Recco`.`users` (`idusers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
