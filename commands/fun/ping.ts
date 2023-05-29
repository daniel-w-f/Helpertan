// const { SlashCommandBuilder } = require('discord.js');

// module.exports = {
// 	data: new SlashCommandBuilder()
// 		.setName('ping')
// 		.setDescription('Replies with Pong!'),
// 	async execute(interaction) {
// 		await interaction.reply('Pong!');
// 	},
// };

// export {};

const { SlashCommandBuilder } = require('discord.js');

const data = new SlashCommandBuilder()
	.setName('ping')
	.setDescription('Replies with Pong!');

async function execute(interaction) {
	await interaction.reply('Pong!');
};

export { data, execute };
