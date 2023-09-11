
#include <iostream>
using namespace std;

//给定一组任务,每个任务有前置任务，需要完成前置任务才能完成下一个任务
//{0,1}表示0是1的前置任务，需要先完成0才能完成1
//给定输入序列，如果能完成所有任务输出 YES 否则输出NO

//示例输入：{{0,1},{1,2},{2,3}}
//示例输出: NO


//思路：拓扑排序，判断是否有环


#include <iostream>
#include <queue>
#include <vector>
using namespace std;

bool solution(vector<vector<int>>input)
{
    int n = input.size();
    vector<int>indegree(n, 0);
    vector<vector<int>>graph(n, vector<int>());
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < input[i].size(); j++) {
            graph[input[i][j]].push_back(i);
            indegree[i]++;
        }
    }
    queue<int>q;
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }
    int count = 0;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        count++;
        for (int i = 0; i < graph[cur].size(); i++) {
            indegree[graph[cur][i]]--;
            if (indegree[graph[cur][i]] == 0) {
                q.push(graph[cur][i]);
            }
        }
    }
    return count == n;
}

int main() {
    string line;
    cin >> line;
    vector<vector<int>> input;
    int i = 0;
    while (i < line.size()) {
        if (line[i] == '{') {
            vector<int> tmp;
            i++;
            while (line[i] != '}') {
                if (line[i] == ',') {
                    i++;
                    continue;
                }
                tmp.push_back(line[i] - '0');
                i++;
            }
            input.push_back(tmp);
        }
        i++;
    }

    if (solution(input)) {
        cout << "No" << endl;
    } else {
        cout << "YES" << endl;
    }
}