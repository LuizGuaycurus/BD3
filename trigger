
CREATE TRIGGER trg_apos_nova_venda
AFTER INSERT ON Vendas
FOR EACH ROW
BEGIN
    
    SET salario = salario + (NEW.valor_venda * 0.03)
    WHERE id_funcionario = NEW.id_funcionario;
END;


