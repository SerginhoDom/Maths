function answer = countDiferencesInArray(node)
    answer = [];
    for i = 1:length(node)-1
        answer(end + 1) = node(i+1) - node(i);
    end
end