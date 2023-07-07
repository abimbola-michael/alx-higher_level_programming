#include "hash_tables.h"

/**
 * hash_table_set - a function that adds an element to the hash table.
 * @ht: the hash table you want to add or update the key/value to
 * @key: the key. key can not be an empty string
 * @value: the value associated with the key
 * Return: 1 if it succeeded, 0 otherwise
 */

int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	hash_node_t *new_node;
	char *value_dup;
	unsigned long int i, node_index;

	if (ht == NULL|| key == NULL || value == NULL || *key == '\0')
		return (0);

	value_dup = strdup(value);

	if (value_dup == NULL)
		return (0);

	node_index = key_index((const unsigned char *)key, ht->size);

	for (i = node_index; ht->array[i]; i++)
	{
		if (strcmp(ht->array[i].key, key) == 0)
		{
			free(ht->array[i]->value);
			ht->array[i]->value = value_dup;
			return (1);
		}
	}

	new_node = malloc(sizeof(hash_node_t));

	if (new_node == NULL)
	{
		free(value_dup);
		return (0);
	}

	new_node->key = strdup(key);

	if (new_node->key == NULL)
	{
		free(value_dup);
		free(new_node);
		return (0);
	}

	new_node->value = value_dup;
	new_node->next = ht->array[node_index];
	ht->array[node_index] = new_node;

	return (1);
}
