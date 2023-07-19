'use strict';
const { Model } = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class TvShow extends Model {
    static associate(models) {
      // define association here
      models.TvShow.belongsToMany(models.Employee, {
        through: 'TvShowEmployee',
      });
      models.TvShow.belongsToMany(models.Season, { through: 'TvShowSeason' });
    }
  }
  TvShow.init(
    {
      title: DataTypes.STRING,
      description: DataTypes.STRING,
      duration: DataTypes.SMALLINT,
      createdAt: {
        type: DataTypes.DATE,
        defaultValue: new Date(),
        allowNull: false,
      },
      updatedAt: {
        type: DataTypes.DATE,
        defaultValue: new Date(),
        allowNull: false,
      },
    },
    {
      sequelize,
      modelName: 'TvShow',
    }
  );
  return TvShow;
};
