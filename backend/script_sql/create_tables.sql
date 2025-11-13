
CREATE TABLE `demonstracoes_contabeis` (
   `DATA` date DEFAULT NULL,
   `REG_ANS` bigint DEFAULT NULL,
   `CD_CONTA_CONTABIL` varchar(50) DEFAULT NULL,
   `DESCRICAO` varchar(255) DEFAULT NULL,
   `VL_SALDO_INICIAL` decimal(18,2) DEFAULT NULL,
   `VL_SALDO_FINAL` decimal(18,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `operadoras` (
   `REGISTRO_OPERADORA` int DEFAULT NULL,
   `CNPJ` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Razao_Social` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Nome_Fantasia` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Modalidade` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Logradouro` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Numero` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Complemento` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Bairro` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Cidade` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `UF` char(2) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `CEP` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `DDD` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Telefone` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Fax` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Endereco_eletronico` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Representante` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Cargo_Representante` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Regiao_de_Comercializacao` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `Data_Registro_ANS` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `top10_operadoras_ultimo_ano_2024` (
   `Razao_Social` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `REG_ANS` bigint DEFAULT NULL,
   `total_despesas` decimal(40,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `top10_operadoras_ultimo_trimestre_2025` (
   `Razao_Social` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
   `REG_ANS` bigint DEFAULT NULL,
   `total_despesas` decimal(40,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
