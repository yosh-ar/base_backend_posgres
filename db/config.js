const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('finance', 'postgres', 'admin', {
    host: 'localhost', 
    dialect: 'postgres', 
    port: 5432,
  });



function conexion () {
    try {
        await sequelize.sync();
        console.log('Conexión a la base de datos PostgreSQL establecida con éxito.');

      } catch (error) {
        console.error('Unable to connect to the database:', error);
      }
}
  // module.exports = sequelize;