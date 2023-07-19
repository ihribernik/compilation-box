'use strict';
const { Model } = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Season extends Model {
    static associate(models) {
      // define association here
      models.Season.belongsToMany(models.Episode, { through: 'SeasonEpisode' });
      models.Season.belongsTo(models.TvShow, { through: 'TvShowSeason' });
    }
  }
  Season.init(
    {
      title: DataTypes.STRING,
      description: DataTypes.STRING,
      year: DataTypes.STRING,
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
      modelName: 'Season',
    }
  );
  return Season;
};
