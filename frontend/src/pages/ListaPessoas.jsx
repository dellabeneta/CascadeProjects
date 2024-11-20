import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Button,
  Typography,
  Box,
  IconButton,
} from '@mui/material';
import { Edit as EditIcon, Delete as DeleteIcon, Add as AddIcon } from '@mui/icons-material';
import api from '../services/api';

function ListaPessoas() {
  const [pessoas, setPessoas] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    carregarPessoas();
  }, []);

  const carregarPessoas = async () => {
    try {
      const response = await api.get('/pessoas/');
      setPessoas(response.data);
    } catch (error) {
      console.error('Erro ao carregar pessoas:', error);
    }
  };

  const handleEditar = (id) => {
    navigate(`/editar/${id}`);
  };

  const handleDeletar = async (id) => {
    if (window.confirm('Tem certeza que deseja deletar esta pessoa?')) {
      try {
        await api.delete(`/pessoas/${id}`);
        carregarPessoas();
      } catch (error) {
        console.error('Erro ao deletar pessoa:', error);
      }
    }
  };

  const formatarData = (data) => {
    return new Date(data).toLocaleDateString('pt-BR');
  };

  return (
    <Box sx={{ mt: 4 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 2 }}>
        <Typography variant="h4" component="h1">
          Pessoas Cadastradas
        </Typography>
        <Button
          variant="contained"
          color="primary"
          startIcon={<AddIcon />}
          onClick={() => navigate('/cadastrar')}
        >
          Nova Pessoa
        </Button>
      </Box>

      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Nome</TableCell>
              <TableCell>Email</TableCell>
              <TableCell>Telefone</TableCell>
              <TableCell>Data de Nascimento</TableCell>
              <TableCell>Status</TableCell>
              <TableCell align="center">Ações</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {pessoas.map((pessoa) => (
              <TableRow key={pessoa.id}>
                <TableCell>{pessoa.nome}</TableCell>
                <TableCell>{pessoa.email}</TableCell>
                <TableCell>{pessoa.telefone}</TableCell>
                <TableCell>{formatarData(pessoa.data_nascimento)}</TableCell>
                <TableCell>{pessoa.ativo ? 'Ativo' : 'Inativo'}</TableCell>
                <TableCell align="center">
                  <IconButton
                    color="primary"
                    onClick={() => handleEditar(pessoa.id)}
                  >
                    <EditIcon />
                  </IconButton>
                  <IconButton
                    color="error"
                    onClick={() => handleDeletar(pessoa.id)}
                  >
                    <DeleteIcon />
                  </IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
}

export default ListaPessoas;
