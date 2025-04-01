-- Criação da tabela
CREATE TABLE operadoras(
    DATA DATE NOT NULL,
    REG_ANS INT NOT NULL,
    CD_CONTA_CONTABIL BIGINT NOT NULL UNIQUE,
    DESCRICAO VARCHAR(255),
    VL_SALDO_INICIAL DECIMAL(15, 2),
    VL_SALDO_FINAL DECIMAL(15, 2),
    INDEX idx_reg_ans (REG_ANS),
    INDEX idx_data (DATA)
);

DELIMITER //
CREATE PROCEDURE carregar_todos_arquivos()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE file_path VARCHAR(255);
    
    WHILE i <= 8 DO
        SET file_path = CONCAT('dados/T', i, '.csv');
        
        SET @sql = CONCAT("
            LOAD DATA INFILE '", file_path, "'
            INTO TABLE operadoras
            CHARACTER SET utf8
            FIELDS TERMINATED BY '\t'
            ENCLOSED BY '\"'
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS
            (@data_var, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
            SET data = STR_TO_DATE(@data_var, '%d/%m/%Y');
        ");
        
        PREPARE stmt FROM @sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
        
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

-- Execute o procedimento
CALL carregar_todos_arquivos();