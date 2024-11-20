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
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  DialogContentText,
} from '@mui/material';
import { Edit as EditIcon, Delete as DeleteIcon, Add as AddIcon } from '@mui/icons-material';
import api from '../services/api';

function ListaPessoas() {
  const [pessoas, setPessoas] = useState([]);
  const [deleteDialog, setDeleteDialog] = useState(false);
  const [pessoaParaDeletar, setPessoaParaDeletar] = useState(null);
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

  const handleAbrirDeleteDialog = (pessoa) => {
    setPessoaParaDeletar(pessoa);
    setDeleteDialog(true);
  };

  const handleFecharDeleteDialog = () => {
    setDeleteDialog(false);
    setPessoaParaDeletar(null);
  };

  const handleConfirmarDelete = async () => {
    if (pessoaParaDeletar) {
      try {
        await api.delete(`/pessoas/${pessoaParaDeletar.id}`);
        handleFecharDeleteDialog();
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
      <Box sx={{ 
        display: 'flex', 
        justifyContent: 'space-between', 
        mb: 2,
        alignItems: 'center',
        '& > button': {
          marginLeft: 2,
          marginRight: '80px'
        }
      }}>
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
                    onClick={() => handleAbrirDeleteDialog(pessoa)}
                  >
                    <DeleteIcon />
                  </IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      {/* Diálogo de confirmação de exclusão */}
      <Dialog
        open={deleteDialog}
        onClose={handleFecharDeleteDialog}
        aria-labelledby="delete-dialog-title"
        aria-describedby="delete-dialog-description"
      >
        <DialogTitle id="delete-dialog-title">
          Confirmar Exclusão
        </DialogTitle>
        <DialogContent>
          <DialogContentText id="delete-dialog-description">
            Tem certeza que deseja excluir {pessoaParaDeletar?.nome}? 
            Esta ação não poderá ser desfeita.
          </DialogContentText>
        </DialogContent>
        <DialogActions sx={{ padding: 2 }}>
          <Button 
            onClick={handleFecharDeleteDialog}
            variant="outlined"
          >
            Cancelar
          </Button>
          <Button 
            onClick={handleConfirmarDelete}
            variant="contained"
            color="error"
            autoFocus
          >
            Excluir
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}

export default ListaPessoas;
