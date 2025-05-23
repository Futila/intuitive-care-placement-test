SELECT 
    REG_ANS,
    SUM(VL_SALDO_FINAL - VL_SALDO_INICIAL) AS DESPESA_TOTAL
FROM 
    operadoras
WHERE 
    DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS' or DESCRICAO = 'AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
    AND DATA >= DATE_SUB(DATE_FORMAT(CURRENT_DATE, '%Y-%m-01'), INTERVAL 3 MONTH)
    AND (VL_SALDO_FINAL - VL_SALDO_INICIAL) > 0
GROUP BY 
    REG_ANS
ORDER BY 
    DESPESA_TOTAL DESC
LIMIT 10;

---------------------------------------------------------------------------------
SELECT 
    REG_ANS,
    SUM(VL_SALDO_FINAL - VL_SALDO_INICIAL) AS DESPESA_ANUAL
FROM 
    operadoras
WHERE 
    DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS' or DESCRICAO = 'AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
    AND DATA >= DATE_SUB(DATE_FORMAT(CURRENT_DATE, '%Y-%m-01'), INTERVAL 1 YEAR)
    AND (VL_SALDO_FINAL - VL_SALDO_INICIAL) > 0
GROUP BY 
    REG_ANS
ORDER BY 
    DESPESA_ANUAL DESC
LIMIT 10;