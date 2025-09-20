from sklearn import preprocessing


def kfold_split(number_of_splits: int = 5) -> list[dict[str, list]]:
    iterations_train_test_indexes = [
        {
            'train': [j for j in range(i)] +
            [j for j in range(i+1, number_of_splits)],
            'test': [i]
            # ik this is stupid it's just to much types inside a dict
        }
        for i in range(number_of_splits)
    ]
    return iterations_train_test_indexes

    
def split_arr(arr: list, number_of_splits: int = 5) -> list[list]:
    k, m = divmod(len(arr), number_of_splits)
    return list(
        arr[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(number_of_splits)
    )
    
def flat_once(arr: list[list]) -> list:
    return [el for subarr in arr for el in subarr]


def knn_cv_score(x, y, iterations_train_test_indexes: list[dict[str, list]],
    knn_class, metric, weights, normalizer, score_func,
    number_of_splits: int = 5, number_of_neighbors: int = 4):

    splitted_X = split_arr(x, number_of_splits)
    splitted_y = split_arr(y, number_of_splits)
    
    score = 0
    if normalizer:
        for i in range(number_of_splits):
            neigh = knn_class(n_neighbors=number_of_neighbors,
                weights=weights, metric=metric, n_jobs=-1)
            current_indexes = iterations_train_test_indexes[i]
            
            neigh.fit(
                normalizer.fit_transform(flat_once(
                    [el for j, el in enumerate(splitted_X)
                    if j in current_indexes['train']])),
                flat_once([el for j, el in enumerate(splitted_y)
                    if j in current_indexes['train']])
            )
        
            score += score_func(
                neigh.predict(normalizer.transform(splitted_X[i])),
                splitted_y[i])
            
    else:
        for i in range(number_of_splits):
            neigh = knn_class(n_neighbors=number_of_neighbors,
                weights=weights, metric=metric, n_jobs=-1)
            current_indexes = iterations_train_test_indexes[i]
            
            neigh.fit(
                flat_once([el for j, el in enumerate(splitted_X)
                    if j in current_indexes['train']]),
                flat_once([el for j, el in enumerate(splitted_y)
                    if j in current_indexes['train']])
            )
        
            score += score_func(
                neigh.predict(splitted_X[i]), splitted_y[i])
        
    return score / number_of_splits
