#include "hash_tables.h"

/**
 * hash_table_delete - a function that deletes a hash table.
 * @ht: the hash table
 */

void hash_table_delete(hash_table_t *ht)
{
	hash_node_t *node;
	undsigned int i;

	for (i = 0; i < ht->size; i++)
	{
		if (ht->array[i] != NULL)
		{
			node = ht->array[i];
			while (node)
			{
				free(node->key);
				free(node->value);
				free(node);
				node = node->next;
                        }
                }
        }
	free(ht->array);
	free(ht);
}
