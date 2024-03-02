/* Author: Steffen Viken Valvaag <steffenv@cs.uit.no> */
#include "list.h"
#include "set.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include "common.h"
#include "printing.h"

/*
 * Case-insensitive comparison function for strings.
 */
static int compare_words(void *a, void *b)
{
    return strcasecmp(a, b);
}

/*
 * Returns the set of (unique) words found in the given file.
 */
static set_t *tokenize(char *filename)
{
	set_t *wordset = set_create(compare_words);
	list_t *wordlist = list_create(compare_words);
	list_iter_t *it;
	FILE *f;
	
	f = fopen(filename, "r");
	if (f == NULL) {
		perror("fopen");
		ERROR_PRINT("fopen() failed");
	}
	tokenize_file(f, wordlist);
	
	it = list_createiter(wordlist);
	while (list_hasnext(it)) {
		set_add(wordset, list_next(it));		
	}
	list_destroyiter(it);
	list_destroy(wordlist);
	return wordset;
}

/*
 * Prints a set of words.
 */
static void printwords(char *prefix, set_t *words)
{
	set_iter_t *it;
	
	it = set_createiter(words);
	INFO_PRINT("%s: ", prefix);
	while (set_hasnext(it)) {
		INFO_PRINT(" %s", (char *)set_next(it));
	}
	printf("\n");
	set_destroyiter(it);
}

/*
 * Main entry point.
 */
int main(int argc, char **argv)
{
	// Creates strings for the spam, nonspam and mail
	char *spamdir, *nonspamdir, *maildir;
	
	
	if (argc != 4) {
		DEBUG_PRINT("usage: %s <spamdir> <nonspamdir> <maildir>\n", argv[0]);
		return 1;
	}
	spamdir = argv[1];
	nonspamdir = argv[2];
	maildir = argv[3];

	// Making list containing the spam and non spam files
	list_t *spam = find_files(spamdir);
	list_t *nonspam = find_files(nonspamdir);
	list_iter_t *spamit = list_createiter(spam);
	list_iter_t *nonspamit = list_createiter(nonspam);

	// Making sets for spam and nonspam
	set_t *intersection_spamset = tokenize(list_next(spamit));
	set_t *union_nonspamset = tokenize(list_next(nonspamit));
	set_t *spamset, *nonspamset;

	// Creating the intersection set of all the spam files
	while(list_hasnext(spamit)){
		spamset = tokenize(list_next(spamit));
		intersection_spamset = set_intersection(spamset, intersection_spamset);
	}

	// Creating the union set of all the nonspam files
	while(list_hasnext(nonspamit)){
		nonspamset = tokenize(list_next(nonspamit));
		union_nonspamset = set_union(nonspamset, union_nonspamset);
	}

	// Destroying the sets to avoid memory leaks
	set_destroy(spamset);
	set_destroy(nonspamset);

	// Creating a list of the mail files
	list_t *maillist = find_files(maildir);
	list_iter_t *mailit = list_createiter(maillist);

	// Creating sets to find the difference of the sets and comparing to mail set
	set_t *intset, *diffset, *mailset;

	while(list_hasnext(mailit)){
		// Finding the possible spamwords in the mails
		void *listnames = list_next(maillist);
		mailset = tokenize(list_next(mailit));
		intset = set_intersection(mailset, intersection_spamset);
		diffset = set_difference(intset, union_nonspamset);
		
		// Printing the mails, number of spamwords, and if they are spam or not
		printf("%s: %d spam word(s) -> %s\n", listnames, set_size(diffset), (set_size(diffset) > 0) ? "SPAM" : "NOT SPAM");
		set_destroy(mailset);
		set_destroy(intset);
		set_destroy(diffset);
	}

	// Destroying all the sets, lists and iterators to avoid memory leaks
	set_destroy(union_nonspamset);
	set_destroy(intersection_spamset);
	list_destroy(maillist);
	list_destroy(spam);
	list_destroy(nonspam);
	list_destroyiter(mailit);
	list_destroyiter(spamit);
	list_destroyiter(nonspamit);

    return 0;
}
